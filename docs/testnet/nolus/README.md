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
peers="785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,3c4f8aa4bf226c331b32d93f51f089e47e753279@194.163.155.84:36656,a7a48a15db2140201f22047ee9abbc0b259c1f92@194.163.129.102:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,621c459c333de1a03250bb846647fc858b9c8638@38.242.142.83:26656,805f69593aeb23e78ae19b4adca24d0ddd513e12@38.242.141.147:26656,71cb32264e19b25fc313d0ff8baf24fe948576a1@65.109.30.12:60656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
