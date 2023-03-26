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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,7e36c0540c2b8fa6032acbf1d02bd5ea02d39246@198.199.70.10:26656,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,4a369367f8ee97c976330f9be79da387d11a0340@65.108.194.44:28656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
