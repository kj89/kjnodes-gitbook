# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (9)
```bash
peers="ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656,38a546d75ae84bb002990ce2eb35c04d7d284809@159.223.69.214:26656,dff203d0633c98eea4a228c5e913f22236043d89@23.88.69.101:16656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,a478235ecd296f14a2889fac5eb4b43e5e98c239@159.69.64.22:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
