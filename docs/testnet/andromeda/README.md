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
peers="94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,49dba71ee0851836601a63577510c82577b057e4@5.135.140.211:30656,20373ec71cffdb678099ca411fb862537f264791@178.172.212.135:26656,50ce639d8889108b488f0aa802468bc13d4873a4@75.119.159.195:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
