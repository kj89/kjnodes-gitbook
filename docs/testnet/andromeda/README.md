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

**live-peers** (12)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
