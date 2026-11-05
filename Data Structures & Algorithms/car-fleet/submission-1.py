class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        time = []
        stack = []

        for i in range(0, len(cars)):

            t = (target - cars[i][0])/cars[i][1]
            time.append(t)

        fleets = 0  
        stack_max = time[0]
        for x in time:
            if len(stack) != 0 and stack_max < x:
                fleets +=1
                while len(stack) !=0:
                    stack.pop()
                stack_max = max(stack_max, x)
            stack.append(x)

        if len(stack)!=0:
            fleets+=1

        return fleets