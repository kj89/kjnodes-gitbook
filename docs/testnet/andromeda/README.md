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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
