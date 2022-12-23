# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


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
peers="0d600b8281ee6a710c213023755d2382cf90af13@116.202.165.116:46656,4a469068099620e1012d8f439b45f6a3a3357027@78.47.97.177:26656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,849d98423e3f757233bef91d7b80937329d7684f@162.19.131.173:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
