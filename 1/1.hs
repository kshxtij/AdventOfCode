import System.IO
import Data.Function

isGreater :: Integer -> Integer -> Integer
isGreater x y
  | y > x     = 1
  | otherwise = 0

countIncreases :: [Integer] -> Integer
countIncreases x = sum $ zipWith isGreater x $ tail x

slidingWindowSum :: Integer -> [Integer] -> [Integer]
slidingWindowSum windowSize list
  | windowSize == 1 = list
  | otherwise       = zipWith (+) list $ slidingWindowSum (windowSize - 1) $ tail list

main :: IO()
main = do
    inputs <- readFile "input.txt"
    let xs = map (\x -> read x::Integer) (lines inputs)
    print $ countIncreases xs
    print $ countIncreases $ slidingWindowSum 3 xs