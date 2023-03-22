# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

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

**live-peers** (15)
```bash
peers="b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,a583f951655a3c9934944d332bb4f6cf7416a3b7@94.131.108.126:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
