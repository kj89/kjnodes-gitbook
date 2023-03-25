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
peers="5e5186020063f7f8a3f3c6c23feca32830a18f33@65.109.174.30:56656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
