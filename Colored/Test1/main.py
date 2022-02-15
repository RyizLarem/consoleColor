from colored import fg, bg, attr

print('%s Hello World !!! %s' % (fg(1), attr(0)))

print('%s%s Hello                %s' % (fg(5), bg(19), attr(1)))
print('%s%s I\'m                  %s' % (fg(9), bg(47), attr(1)))
print('%s%s Ryiz!                %s' % (fg(5), bg(25), attr(1)))
print('%s%s and                  %s' % (fg(5), bg(19), attr(1)))
print('%s%s I am testin          %s' % (fg(5), bg(27), attr(1)))
print('%s%s a colored            %s' % (fg(5), bg(9), attr(1)))
print('%s%s PYTHON cool language %s' % (fg(5), bg(7), attr(1)))
print('%s%s . . .                %s' % (fg(5), bg(8), attr(1)))
print("____________________________________________________________________")
print(fg(13) + bg(7) + attr(24)+ "test  .       .       .")


