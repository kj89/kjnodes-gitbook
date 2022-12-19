# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

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
peers="302466457301efc7b12f61561b85ab366ece5659@142.132.248.253:26656,4a469068099620e1012d8f439b45f6a3a3357027@78.47.97.177:26656,0d600b8281ee6a710c213023755d2382cf90af13@116.202.165.116:46656,0f5c320341a9134743f70f29dc99572977f97161@159.69.201.172:12656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,c932600aa633bb17e07dcb53ae982c834ba1b734@185.225.232.148:26656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
