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
peers="e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,ea0c590882f4fa490a4563e364d341e078ad138e@94.131.105.228:26656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,08da04e20e295f48518d095871ba5c13e58c3dfd@185.209.223.64:36656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
