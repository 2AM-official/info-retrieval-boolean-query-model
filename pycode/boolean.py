import math

class BooleanModel():

    def and_operation(left_operand, right_operand):
        result = []
        l_idx = 0
        r_idx = 0
        # l_skip = int(math.sqrt(len(left_operand)))
        # r_skip = int(math.sqrt(len(right_operand)))

        while l_idx < len(left_operand) and r_idx < len(right_operand):
            l_item = left_operand[l_idx]
            r_item = right_operand[r_idx]

            if l_item == r_item:
                result.append(l_item)
                l_idx += 1
                r_idx += 1

            elif l_item > r_item:
                r_idx += 1

            else:
                l_idx += 1
        #print(result)
        return result
    
    def or_operation(left_operand, right_operand):
        result = []
        l_idx = 0
        r_idx = 0

        while l_idx < len(left_operand) or r_idx < len(right_operand):
            if l_idx < len(left_operand) and r_idx < len(right_operand):
                l_item = left_operand[l_idx]
                r_item = right_operand[r_idx]

                if l_item == r_item:
                    result.append(l_item)
                    l_idx += 1
                    r_idx += 1
                
                elif l_item > r_item:
                    result.append(r_item)
                    r_idx += 1
                else:
                    result.append(l_item)
                    l_idx += 1
            elif l_idx >= len(left_operand):
                r_item = right_operand[r_idx]
                result.append(r_item)
                r_idx += 1
            
            else:
                l_item = left_operand[l_idx]
                result.append(l_item)
                l_idx += 1
        return result

    def not_operation(right_operand, number_of_tweets):
        if not right_operand:
            return number_of_tweets
        
        result = []
        r_idx = 0
        for item in number_of_tweets:
            if item != right_operand[r_idx]:
                result.append(item)
            elif r_idx + 1 < len(right_operand):
                r_idx += 1
        return result