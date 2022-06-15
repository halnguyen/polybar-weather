<h1>Weather Plugin</h1>

A small python script to display weather information on polybar

<h3>Dependencies and requirements</h3>

<ul>
	<li><a href="https://github.com/polybar/polybar">Polybar</a></li>
	<li>Python3</li>
	<li><a href="https://pypi.org/project/requests/">requests</a></li>
</ul>

<h3>Instructions</h3>

<ol>
	<li>
		Run <code>pip3 show requests</code>, if no package is found, run <code>pip3 install request</code>.
	</li>
	<li>
		Clone this repo and note of the location, the weather.py file will need to be added to polybar as a <a href="https://github.com/polybar/polybar/wiki/Module:-script">custom script module</a>.
	</li>
	<li>
		Before the code can run, an <a href="https://openweathermap.org/">OpenWeather API key</a> is needed, along with latitude and the longitude of the location.
	</li>
	<li>
		Update the file resource.json accordingly. Reminder that the lat, lon and api key are wrapped in double quotes.
	</li>
</ol>
