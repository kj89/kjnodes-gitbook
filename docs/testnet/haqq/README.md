# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```
peers="ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,0ba87cb7b55b15e6b33b6703dc681c84332273e5@168.119.165.65:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,d5fe19a11f4b4a138da9b2bc3fbe6031182538a0@135.181.133.37:30656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,022360b6d3bbae324b0cca90f80f6322576e2b42@135.181.109.140:12656,5e0ba89aed3b21f7ae56877da9bd0a5a0d3736d5@168.119.186.161:26656,cf3127b52249fce3859a42afeb4162d6788593e2@77.232.39.155:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
