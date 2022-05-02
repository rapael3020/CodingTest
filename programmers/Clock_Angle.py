def solution(hour, minute):
    h = (360/12)*hour + (360/12/60)*minute
    m = (360/60)*minute
    
    ans = abs(h-m)
    if ans > 180:
        ans = 360 - ans
    ans = f'{ans:.1f}'
    return ans