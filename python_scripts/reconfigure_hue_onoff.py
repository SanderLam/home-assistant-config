ieees = data.get("ieees")

for ieee in ieees:
      service_data1 = {
            'ieee': ieee,
            'endpoint_id': 11,
            'cluster_id': 6,
            'cluster_type': 'in',
            'attribute': 16387,
            'value': 255
      }
      hass.services.call('zha', 'set_zigbee_cluster_attribute', service_data1, False)
      logger.info("Service data 1 called")
      time.sleep(5)
      service_data2 = {
            'ieee': ieee,
            'endpoint_id': 11,
            'cluster_id': 8,
            'cluster_type': 'in',
            'attribute': 16384,
            'value': 255
      }
      hass.services.call('zha', 'set_zigbee_cluster_attribute', service_data2, False)
      logger.info("Service data 2 called")
      time.sleep(5)
      service_data3 = {
            'ieee': ieee,
            'endpoint_id': 11,
            'cluster_id': 768,
            'cluster_type': 'in',
            'attribute': 16400,
            'value': 65535
      }
      hass.services.call('zha', 'set_zigbee_cluster_attribute', service_data3, False)
      logger.info("Service data 3 called")
      time.sleep(5)
      service_data4 = {
            'ieee': ieee,
            'endpoint_id': 11,
            'cluster_id': 768,
            'cluster_type': 'in',
            'attribute': 3,
            'value': 65535
      }
      hass.services.call('zha', 'set_zigbee_cluster_attribute', service_data4, False)
      logger.info("Service data 4 called")
      time.sleep(5)