---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/umee.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: umee-1 | **Latest Version Tag**: v5.0.1 | **Custom Port**: 162

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf umee
git clone https://github.com/umee-network/umee.git
cd umee
git checkout v5.0.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.umee/cosmovisor/upgrades/v5.0/bin
mv build/umeed $HOME/.umee/cosmovisor/upgrades/v5.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
