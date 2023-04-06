# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (29)
```bash
peers="8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,758641fe59d2d80061a1695a82fbcec12d8b6c54@185.209.230.110:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,bc3f9bf7c5384496f053d15327f26d9ac1451b3d@149.102.136.149:26656,e25aed855f59ad20e44859111f0547be764db21c@154.12.229.17:26656,719ff70668a75940daf2f2beb30b60986301557a@34.92.222.72:26656,b7369fd18787142993c984002fa0a9defabf61dd@45.151.122.39:26656,88086a2be6373563afff389c383abc6aaaeee178@161.97.142.46:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,c03ac8a54e2fe73ac59d621eb0262456eca4d3d8@83.169.217.43:39656,6d74d38dfeb41764d1544e0e01a50240c13d9b2c@38.242.232.30:26656,bf1b17b374d1bbe3e496ae604f8416e04fa2091f@84.46.247.234:26656,6321aa1766906887c46745d57ddc38d688b2a625@85.208.51.131:39656,b66a727b45c7859b395bbe6f634711dcad7bc557@31.220.88.121:26656,049b792991a67c8c50e94489645bb9bc4bd5f8fa@80.85.242.48:26656,ed66095b43d923ecdc73eb77d6193084036888bc@65.108.2.35:26656,a3cdb006b290cd2e694b451e8e141ee397a24eac@85.190.246.96:26656,6a822c4729b1ab9434a85489d2cd14556e416632@165.232.64.79:26656,66c9b3dd0eb74c02010c286304f80f39994c89ed@109.123.244.119:26656,113236026b32b6f59b7b95cbead6dd77c1dd18f9@185.202.223.253:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
