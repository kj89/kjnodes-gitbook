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

**live-peers** (9)
```
peers="17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,7d1ac536c8451d1b64e9702fb172ac5b1b725778@65.109.85.221:9000,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,3043450abbb1026c2e73d8a2549ee2e395ea5454@65.108.78.41:36656,36bf6f60f2914352c93dcc6d827885e3e58b1f2b@158.160.20.18:26656,ef404b6e855c70ee51532ca83407350d2379bdec@5.161.101.185:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,e95c1138763c637ca62a391bc316c9a96283d79f@188.40.122.98:36656,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
