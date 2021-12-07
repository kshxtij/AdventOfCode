import Data.List.Split

day :: [Int] -> [Int]
day [a, b, c, d, e, f, g, h, i] = [b, c, d, e, f, g, h + a, i, a]

main :: IO()
main = do
    input <- readFile "input.txt"
    let xs = map (\x -> read x::Int) $ splitOn "," input
    let xs' = map (\x -> (length . filter (== x)) xs) [0..8]
    print $ sum $ iterate day xs' !! 80
    print $ sum $ iterate day xs' !! 256