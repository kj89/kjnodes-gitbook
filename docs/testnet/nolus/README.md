# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


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
peers="e08055aae540efed02e736ec79621f293fe92ae9@65.109.92.240:1176,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,900d1cb2429206af2dea377257cbea0bb27dd625@38.242.233.94:26656,accae890c5c62f83cbb2d541de462065aaf67724@45.87.104.154:37656,721e40c2c9abefa358f9428bc396cdbe05520312@65.109.92.79:16656,9f4512527a9e7eac1847b910f8d4b2c0ef1617de@5.161.180.85:26656,9d761ce1e1dc54ded3ab82ce0256c27631b5e82c@173.212.241.80:43656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,76b961a70249b7967ee51361807b87302178708e@38.242.200.89:26656,36bf6f60f2914352c93dcc6d827885e3e58b1f2b@158.160.20.18:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
