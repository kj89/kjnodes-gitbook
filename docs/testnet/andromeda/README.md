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
peers="0da5e83ef55df6f1c6f8c15c69bdd42ee43fd253@144.76.99.100:30656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
