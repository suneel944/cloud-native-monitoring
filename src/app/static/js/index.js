const source = new EventSource('/dashboard-data');

source.onmessage = function(event) {
    const data = JSON.parse(event.data);
    /* Element queries */
    const cpu_percentage = document.getElementById("cpu_usage_percentage");
    const cpu_count = document.getElementById("cpu_count");
    const cpu_frequency = document.getElementById("cpu_frequency");

    const memory_usage_percentage = document.getElementById("memory_usage_percentage");
    const total_memory = document.getElementById("total_memory");
    const utilized_memory = document.getElementById("utilized_memory");
    const free_memory = document.getElementById("free_memory");
    const available_memory = document.getElementById("available_memory");
    
    const total_disk_size = document.getElementById("total_disk_size");
    const disk_utilized = document.getElementById("disk_utilized");
    const free_disk_space = document.getElementById("free_disk_space");
    const disk_usage_percentage = document.getElementById("disk_usage_percentage");
    
    const total_swap_memory = document.getElementById("total_swap_memory");
    const utilized_swap_memory = document.getElementById("utilized_swap_memory");
    const free_swap_memory = document.getElementById("free_swap_memory");
    const used_swap_memory_percentage = document.getElementById("used_swap_memory_percentage");
    
    const network_io_counters_bytes_sent = document.getElementById("network_io_counters_bytes_sent");
    const network_io_counters_bytes_received = document.getElementById("network_io_counters_bytes_received");
    const network_io_counters_packets_sent = document.getElementById("network_io_counters_packets_sent");
    const network_io_counters_packets_received = document.getElementById("network_io_counters_packets_received");
    const network_io_counters_errin = document.getElementById("network_io_counters_errin");
    const network_io_counters_errout = document.getElementById("network_io_counters_errout");
    const network_io_counters_dropin = document.getElementById("network_io_counters_dropin");
    const network_io_counters_dropout = document.getElementById("network_io_counters_dropout");
    /* Update dashboard with new system data */
    /* CPU */
    if(data.cpu_percentage) {
        cpu_percentage.textContent = (data.cpu_percentage);
    } else {
        cpu_percentage.textContent = "N/A";
    }
    if(data.cpu_count) {
        cpu_count.textContent = (data.cpu_count);
    } else {
        cpu_count.textContent = "N/A";
    }
    if(data.cpu_frequency.current) {
        cpu_frequency.textContent = (data.cpu_frequency.current).toFixed(2);
    } else {
        cpu_frequency.textContent = 'N/A';
    }
    /* Memory */
    if(data.memory) {
        memory_usage_percentage.textContent = (data.memory.percentage);
        total_memory.textContent = (data.memory.total / 1e+9).toFixed(2);
        utilized_memory.textContent = (data.memory.used / 1e+9).toFixed(2);
        free_memory.textContent = (data.memory.free / 1e+9).toFixed(2);
        available_memory.textContent = (data.memory.available / 1e+9).toFixed(2);
    } else {
        memory_usage_percentage.textContent = "N/A";
        total_memory.textContent = "N/A";
        utilized_memory.textContent = "N/A";
        free_memory.textContent = "N/A";
        available_memory.textContent = "N/A";
    }
    /* Disk Usage */
    if(data.disk_usage) {
        total_disk_size.textContent = (data.disk_usage.total / 1e+9).toFixed(2);
        disk_utilized.textContent = (data.disk_usage.used / 1e+9).toFixed(2);
        free_disk_space.textContent = (data.disk_usage.free / 1e+9).toFixed(2);
        disk_usage_percentage.textContent = (data.disk_usage.percentage);

    } else {
        total_disk_size.textContent = "N/A";
        disk_utilized.textContent = "N/A";
        free_disk_space.textContent = "N/A";
        disk_usage_percentage.textContent = "N/A";
    }
    /* Swap Memory */
    if(data.swap) {
        total_swap_memory.textContent = (data.swap.total / 1e+9).toFixed(2);
        utilized_swap_memory.textContent = (data.swap.used / 1e+9).toFixed(2);
        free_swap_memory.textContent = (data.swap.free / 1e+9).toFixed(2);
        used_swap_memory_percentage.textContent = (data.swap.percentage / 1e+9).toFixed(2);

    } else {
        total_swap_memory.textContent = "N/A";
        utilized_swap_memory.textContent = "N/A";
        free_swap_memory.textContent = "N/A";
        used_swap_memory_percentage.textContent = "N/A";
    }
    /* Network */
    if(data.network_io_counters) {
        network_io_counters_bytes_sent.textContent = (data.network_io_counters.bytes_sent / 1e+9);
        network_io_counters_bytes_received.textContent = (data.network_io_counters.bytes_recv / 1e+9);
        network_io_counters_packets_sent.textContent = (data.network_io_counters.packets_sent);
        network_io_counters_packets_received.textContent = data.network_io_counters.packets_recv;
        network_io_counters_errin.textContent = data.network_io_counters.errin;
        network_io_counters_errout.textContent = data.network_io_counters.errout;
        network_io_counters_dropin.textContent = data.network_io_counters.dropin;
        network_io_counters_dropout.textContent = data.network_io_counters.dropout;


    } else {
        network_io_counters_bytes_sent.textContent = "N/A";
        network_io_counters_bytes_received.textContent = "N/A";
        network_io_counters_packets_sent.textConten = "N/A";
        network_io_counters_packets_received.textContent = "N/A";
        network_io_counters_errin.textContent = "N/A";
        network_io_counters_errout.textContent = "N/A";
        network_io_counters_dropin.textContent = "N/A";
        network_io_counters_dropout.textContent = "N/A";
    }
};
