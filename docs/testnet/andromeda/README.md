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

**live-peers** (16)
```bash
peers="360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,ef30bb942109dbb6d1a13c3c32c46459689a6c15@162.55.245.219:19656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
