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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,e08055aae540efed02e736ec79621f293fe92ae9@65.109.92.240:1176,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,535ca6f6a016261b66ea32c693be35cc3c209414@185.217.125.35:26656,db05aaa5ee2d67f3418cd77df4307f2bb412ee40@65.108.199.62:19656,b707384941f6ae2c291d7031b51771c470e3a686@65.108.9.230:28656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,65145d3500c535aaa66984b188c90aa7a6a8b51c@167.235.192.148:21656,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
