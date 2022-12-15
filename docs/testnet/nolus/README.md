# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

Website: [https://www.nolus.io](https://www.nolus.io)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```
peers="17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,fd13b67b442e1798c4fc3ecc8a81513de149552e@213.239.215.77:34656,1a0bb6c35e2663202535d4b849ff06250762d299@213.239.216.252:35656,33d485f51f413fd4bf83ef8a971c10228a39cffb@62.171.161.172:26656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,3043450abbb1026c2e73d8a2549ee2e395ea5454@65.108.78.41:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,3c4f8aa4bf226c331b32d93f51f089e47e753279@194.163.155.84:36656,81944abef95fcc39da818c458f0e0afab41d2f81@65.109.131.71:56656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
