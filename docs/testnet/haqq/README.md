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
peers="7e45021be5e7754b62b6016305ba26f8bf40beda@142.132.199.27:20116,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,efc12714ae801dcb228e79cf3980b8b8f4b86a88@148.251.53.202:36656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
