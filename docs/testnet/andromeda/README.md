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

**live-peers** (15)
```bash
peers="0fd8550e58b1e450b40032e17ca6d685f7be1c53@217.160.201.92:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,b5743b2e9c811ed2211246721652a996977e8895@65.109.85.226:3340,ea0c590882f4fa490a4563e364d341e078ad138e@94.131.105.228:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
