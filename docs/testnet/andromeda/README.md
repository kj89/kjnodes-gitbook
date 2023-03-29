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

**live-peers** (13)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,49dba71ee0851836601a63577510c82577b057e4@5.135.140.211:30656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,b9a90655c4235894fe6e1dda4f6697e69648e942@135.181.16.252:35656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
