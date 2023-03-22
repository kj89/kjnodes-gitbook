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

**live-peers** (16)
```bash
peers="ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,50ce639d8889108b488f0aa802468bc13d4873a4@75.119.159.195:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,af5384af4257fdff39a2ee2535a1b74c3e052cad@65.109.229.186:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,a583f951655a3c9934944d332bb4f6cf7416a3b7@94.131.108.126:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
