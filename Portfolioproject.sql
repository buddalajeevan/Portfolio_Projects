SELECT * FROM PortfolioProject.NashvilleHousing;

SELECT SaleDate AS SaleDateConverted, DATE(SaleDate) AS SaleDateConverted
FROM PortfolioProject.NashvilleHousing;

#UPDATE PortfolioProject.NashvilleHousing
#SET SaleDate = DATE(SaleDate);

ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN SaleDateConverted DATE;

UPDATE PortfolioProject.NashvilleHousing
SET SaleDateConverted = DATE(SaleDate);

-- Populate Property Address data

-- Select query
SELECT *
FROM PortfolioProject.NashvilleHousing
-- WHERE PropertyAddress IS NULL
ORDER BY ParcelID;

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, COALESCE(a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.NashvilleHousing a
JOIN PortfolioProject.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.UniqueID  <> b.UniqueID
Where a.PropertyAddress is null

UPDATE a
SET PropertyAddress = (a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.NashvilleHousing a
JOIN PortfolioProject.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.UniqueID  <> b.UniqueID 
Where a.PropertyAddress is null

--------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)


Select PropertyAddress
From PortfolioProject.NashvilleHousing
--Where PropertyAddress is null
--order by ParcelID

SELECT
  SUBSTRING_INDEX(PropertyAddress, ',', 1) AS Address,
  SUBSTRING_INDEX(PropertyAddress, ',', -1) AS Address
FROM PortfolioProject.NashvilleHousing;

-- Delete column
ALTER TABLE PortfolioProject.NashvilleHousing
DROP COLUMN PropertySplitAddress;


-- Add new column
ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN PropertySplitAddress NVARCHAR(255);

-- Update values for the new column
UPDATE PortfolioProject.NashvilleHousing
SET PropertySplitAddress = SUBSTRING_INDEX(PropertyAddress, ',', 1);

ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN PropertySplitCity NVARCHAR(255);

UPDATE PortfolioProject.NashvilleHousing
SET PropertySplitCity = SUBSTRING_INDEX(PropertyAddress, ',', -1);

Select OwnerAddress
From PortfolioProject.NashvilleHousing;

-- Select query
SELECT
  SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', -1) AS Part3,
  SUBSTRING_INDEX(SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', -2), '.', 1) AS Part2,
  SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', 1) AS Part1
FROM PortfolioProject.NashvilleHousing;


-- Add new column OwnerSplitAddress
ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN OwnerSplitAddress NVARCHAR(255);

-- Update values for OwnerSplitAddress
UPDATE PortfolioProject.NashvilleHousing
SET OwnerSplitAddress = SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', 1) ;

-- Add new column OwnerSplitCity
ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN OwnerSplitCity NVARCHAR(255);

-- Update values for OwnerSplitCity
UPDATE PortfolioProject.NashvilleHousing
SET OwnerSplitCity = SUBSTRING_INDEX(SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', -2), '.', 1) ;

-- Add new column OwnerSplitState
ALTER TABLE PortfolioProject.NashvilleHousing
ADD COLUMN OwnerSplitState NVARCHAR(255);

-- Update values for OwnerSplitState
UPDATE PortfolioProject.NashvilleHousing
SET OwnerSplitState = SUBSTRING_INDEX(REPLACE(OwnerAddress, ',', '.'), '.', -1) ;



-- Change Y and N to Yes and No in "Sold as Vacant" field


Select Distinct(SoldAsVacant), Count(SoldAsVacant)
From PortfolioProject.NashvilleHousing
Group by SoldAsVacant
order by 2




SELECT SoldAsVacant,
    CASE 
        WHEN SoldAsVacant = 'Y' THEN 'Yes'
        WHEN SoldAsVacant = 'N' THEN 'No'
        ELSE SoldAsVacant
		END
FROM PortfolioProject.NashvilleHousing;



Update PortfolioProject.NashvilleHousing
SET SoldAsVacant = CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END

-- Remove Duplicates
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY ParcelID,
                            PropertyAddress,
                            SalePrice,
                            SaleDate,
                            LegalReference
               ORDER BY UniqueID
           ) AS row_num
    FROM PortfolioProject.NashvilleHousing
    ORDER BY ParcelID
) AS subquery
WHERE row_num > 1
ORDER BY PropertyAddress;

DELETE subquery.*
FROM PortfolioProject.NashvilleHousing AS subquery
JOIN (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY ParcelID,
                            PropertyAddress,
                            SalePrice,
                            SaleDate,
                            LegalReference
               ORDER BY UniqueID
           ) AS row_num
    FROM PortfolioProject.NashvilleHousing
    ORDER BY ParcelID
) AS mainquery
ON subquery.UniqueID = mainquery.UniqueID
WHERE mainquery.row_num > 1;

-- Delete Unused Columns



Select *
From PortfolioProject.NashvilleHousing


-- Drop columns
ALTER TABLE PortfolioProject.NashvilleHousing
DROP COLUMN OwnerAddress,
DROP COLUMN TaxDistrict,
DROP COLUMN PropertyAddress,
DROP COLUMN SaleDate;


