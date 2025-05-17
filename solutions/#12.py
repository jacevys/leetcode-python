class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1: 'I', 5: 'V', 10: 'X',
                     50: 'L', 100: 'C', 500: 'D',
                     1000: 'M', 4: 'IV', 9: 'IX',
                     40: 'XL', 90: 'XC', 400: 'CD',
                     900: 'CM'}
        power = 0
        output_array = []
        output_string = ''
#
        while num > 0:
            digit = num % 10
            real_value = digit * pow(10, power)
            min_value = 10000
            temp_string = ''
#
            while real_value > 0:
                if real_value not in dictionary.keys():
                    for key in dictionary.keys():
                        difference = real_value - key

                        if difference > 0:
                            min_value = min(min_value, difference)

                    temp_string += dictionary[real_value - min_value]
                    real_value -= real_value - min_value
                else:
                    temp_string += dictionary[real_value]
                    break

            output_array.append(temp_string)

            num //= 10
            power += 1

        for digit_string in output_array[::-1]:
            output_string += digit_string

        return output_string
#
class Solution_2:
    def intToRoman(self, num: int) -> str:
        dictionary = {1: 'I', 5: 'V', 10: 'X',
                     50: 'L', 100: 'C', 500: 'D',
                     1000: 'M', 4: 'IV', 9: 'IX',
                     40: 'XL', 90: 'XC', 400: 'CD',
                     900: 'CM'}

        string = ''
        index = 0
        key_array = list(dictionary.keys())
        key_array.sort(reverse=True)

        for key in key_array:
            string += (num // key) * dictionary[key]
            num %= key

        return string
#
def main():
    num = 3999
    solution = Solution_2()
    answer = solution.intToRoman(num)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.08.31
(1)success
(2)time: 24 minutes + 52 minutes + 36 minutes
(3)checked
'''
#