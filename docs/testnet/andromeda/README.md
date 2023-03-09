# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (19)
```bash
peers="03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,0fd8550e58b1e450b40032e17ca6d685f7be1c53@217.160.201.92:26656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
