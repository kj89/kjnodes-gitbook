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
peers="0409afd9db164813d8e5f29eb9e0d5edbd3c7ba0@5.189.163.114:26656,89d067dc2a046f7b7c1c787740fff18962bf199f@95.165.149.94:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,986cf051df64fc21a32b7596c7264e51b25ea3dc@65.109.50.189:26656,4d996674f678ebc035165d7d7c894010b32420a2@65.109.69.240:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,a8b07f98f5fcacb358e063d33eeb1d5953e90650@65.108.11.180:33656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
