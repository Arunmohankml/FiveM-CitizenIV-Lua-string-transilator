Citizen.CreateThread(function()
	while true do
		Citizen.Wait(0)
		DisplayTextWithLiteralString(0.5, 0.8, "STRING", "This text will be transilated")-- here "STRING" wont be transilated as its a blacklisted word
	end
end)
