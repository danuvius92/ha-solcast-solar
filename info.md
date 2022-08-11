### Changes
v1.1
- FIX: coordinator.py", line 133, in update_forecast for update_callback in self._listeners: RuntimeError: dictionary changed size during iteration
- this version needs HA 2022.7+ now

v1.0
- forked and changed code to divide all values coming from api by 2


Simple setup.. just need the API key

- This is now as it should be, a 'forecast' integration (it does not graph past data *currently*)
- Forecast includes sensors for "today" and "tomorrow" total production, max hour production and time.. this hour and next production
- Forecast graph info for the next 7 days of data available

Integration contains
  - API Counter             (int)
  - API Last Polled         (date/time)
  - Forecast Next Hour      (Wh)
  - Forecast This Hour      (Wh)
  - Forecast Today          (kWh) (Attributes calculated from 'pv_estimate')
  - Forecast Tomorrow       (kWh) (Attributes calculated from 'pv_estimate')
  - Peak Forecast Today     (Wh)
  - Peak Forecast Tomorrow  (Wh)
  - Peak Time Today         (date/time)
  - Peak Time Tomorrow      (date/time)

![demo](https://user-images.githubusercontent.com/1471841/172541966-cb3f84a9-66bd-4f0f-99de-6d3e52cfd2ba.png)



### Polling Imformation
Solcast has a 50 API poll limit per day.

