---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: stride-1 | **Latest Version Tag**: v9.2.1 | **Custom Port**: 116

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf stride
git clone https://github.com/Stride-Labs/stride.git
cd stride
git checkout v9.2.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.stride/cosmovisor/upgrades/v9/bin
mv build/strided $HOME/.stride/cosmovisor/upgrades/v9/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
