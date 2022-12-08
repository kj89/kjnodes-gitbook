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
peers="849d98423e3f757233bef91d7b80937329d7684f@162.19.131.173:26656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,89d067dc2a046f7b7c1c787740fff18962bf199f@95.165.149.94:29656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,0ba87cb7b55b15e6b33b6703dc681c84332273e5@168.119.165.65:12656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
