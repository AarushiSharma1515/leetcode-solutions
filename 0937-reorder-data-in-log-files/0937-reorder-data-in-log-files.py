class Solution(object):
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                # we have till here done with 3rd rule
        letter_logs.sort(key = lambda x:(x.split()[1:] , x.split()[0]))
# 2nd rule done 
        result = letter_logs + digit_logs #3rd rulr done
        return result