import Data.List.Split

t1 :: [String] -> Int -> Int -> Int 
t1 [] d h     = d*h
t1 (x:xs) d h | command == "forward" = t1 xs d (h + number)
              | command == "up"      = t1 xs (d - number) h
              | command == "down"    = t1 xs (d + number) h
              where
                  [command, number_string] = splitOn " " x
                  number = read number_string::Int

t2 :: [String] -> Int -> Int -> Int -> Int
t2 [] d h a   = d*h
t2 (x:xs) d h a | command == "forward" = t2 xs (d + number*a) (h + number) a
                | command == "up"      = t2 xs d h (a - number)
                | command == "down"    = t2 xs d h (a + number)
                where
                  [command, number_string] = splitOn " " x
                  number = read number_string::Int

main :: IO()
main = do
    input <- readFile "input.txt"
    let x = lines input
    print $ t1 x 0 0 
    print $ t2 x 0 0 0