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

**live-peers** (9)
```
peers="f93085d78df16bbd16a525683af7f857ce1cd983@188.40.98.169:36656,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,acba49be707c31a831a3bca9d9d9f7defcc0bd21@142.132.148.174:26656,ae78cc2328e61c37e4402a5929abb8566f855513@65.108.9.25:26656,064fe9fe19fe5552b2d4922d659466e583f42b22@95.216.2.219:26658,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
