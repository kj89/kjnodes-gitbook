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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,3dec6d1f84e989d97379f7acaa3036e9ad5e2652@83.171.248.175:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,f2a9fa9880d31a89354250d42dd7cae5364461c7@178.20.42.155:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,534404f68807e4f79ce91d7c5f85c7a974ec2960@185.252.235.250:26656,afe8c5af90e2eef4a98bc998366e2e780a927599@65.108.126.46:34656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
