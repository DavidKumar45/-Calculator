
int $r;
int $fnum;
int $snum;
$a = "y";
$o = 0;

while ($a eq "y") {

print "whats the first number?\n";
$fnum = <>;
print "whats the second number?\n";
$snum = <>;
print "whats the operation?\n";
$o = <>;
chomp($o);

if ($o == "+") {
	$r = $fnum + $snum;
}
elsif ($o == "-") {
	$r = $fnum - $snum;
}
elsif ($o == "*") {
	$r = $fnum * $snum;
}
elsif ($o == "/") {
	$r = $fnum / $snum;
}

print "$r \n";
print "Type Y to do another calculation. Type N to quit.\n";
$a = <>;
chomp ($a);
}
