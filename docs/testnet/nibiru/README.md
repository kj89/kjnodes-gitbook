# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

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

**live-peers** (35)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a71248b62555f3271df17fb476475cfc7db89275@84.46.240.197:26656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,8fd1ceb4bb0ee932025bfdc96e04b87c3a084827@185.135.137.212:26656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,719e5c2c79f027c65514d70e0f08d754119a6f0c@45.10.154.246:26656,cf29df0bc1d8a1d9053d7dc6bd7b8ee69b3021cc@51.89.47.31:26656,b502caa5e8071c14179c562a328bb2a096f6b44a@141.94.139.233:30656,6e4e946ca9a0f01e6c4123fb49575615a629c90b@65.109.111.159:26656,09c05898d64d2ec387e27ae3e1029a2f53a2a1dc@155.133.22.109:26656,7e465cf7525009fa55c8387eb74a330d3b96e26f@86.48.5.78:26656,8e395e5a6082503480bde92720674546f4f1df36@135.181.208.169:26656,9ce8b0b6a93612c9c9dc742413e3a0ac53390246@207.180.229.107:26656,9e05e4a15d6077088cbd84fa5a4311e71556e67a@62.141.37.231:26656,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,0c3c0b937a1f8054794cacd744bf1a13b341508b@113.53.82.252:36656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,8aad729b8ec0e3210b69f4f60b5168606471d3fd@38.242.252.80:26656,c11f38f2ed08253c03e108604e50c503427060f5@66.94.120.204:39656,fd274e8c17b4db13d67be3ef24d7a6c73caa8075@38.242.252.49:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,3030536f218c76eb43d05035ac64dda277cdc14d@109.172.45.7:26656,bc6a9f58cf8abcb3d98848042a1f10720505321e@88.99.68.55:26656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,8213f67d6cdeaf11742f5d454d4d687023ef2941@5.9.61.237:21656,2dcd2d9b6df2191cba36ae0ca193deebc0c6e60b@38.242.217.12:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,199a18ce36a79db678abdbb8b767a2792e239101@165.22.212.57:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
