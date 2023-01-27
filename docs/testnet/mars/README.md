# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="77c8fe95cc4a1b977e03bda41f47a4fa3e867895@185.202.236.112:20656,5bca99161a02e45e9e3fe6303728f8fd13d3d9d8@65.108.69.68:26757,59411839064d29a76e76b4cd9e8d1c221c2bab95@65.21.251.246:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,635bdf5d3fe3b4f28582946cded3513214ff7e24@194.146.13.36:26656,9a191e8b191d1c8e36176b508b9f71f31677f9f8@15.204.207.117:26656,8acb52f684ec6adf59b8a5dcda4d50278b078367@65.109.52.56:22656,aea09eb8f366e388ca74e3f3ffe6909d5c89d1b9@95.214.55.155:22656,5dac2a64e4aea39e3704d551441938a504134e95@194.113.106.81:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
