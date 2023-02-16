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

**live-peers** (36)
```bash
peers="b502caa5e8071c14179c562a328bb2a096f6b44a@141.94.139.233:30656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,cf29df0bc1d8a1d9053d7dc6bd7b8ee69b3021cc@51.89.47.31:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,719e5c2c79f027c65514d70e0f08d754119a6f0c@45.10.154.246:26656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,4cf093f546f665f0c6b6799b42f0bc8bbe4b9ce3@185.215.180.237:26656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,a71be69ab3cae88b9100cc357163e003b11291d1@155.133.22.116:26656,bbc65f7d38f5528cebea9a85020fec5702736da4@94.50.236.105:26656,09c05898d64d2ec387e27ae3e1029a2f53a2a1dc@155.133.22.109:26656,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,3a88426d413c9f7794485bdeab5e1cfda1c7430f@77.232.43.194:26656,fd274e8c17b4db13d67be3ef24d7a6c73caa8075@38.242.252.49:26656,9886bde397f0aaf4c9402e618b49393746266c3a@62.141.39.134:26656,f5dcecad06399db3658bfadc2e3d2e8533305d13@135.125.214.61:26656,73c2805511a8fb700eae740299005c2ff33ec855@45.89.127.44:26656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,656465577c4a24380265725e17bffcd13816d6bc@84.46.246.196:26656,32c587c3d9329e6c13c5cd7797eb46b30b628bca@91.107.132.237:26656,aa3261d279f300aad20cb30262c910884c3a5b05@178.20.41.240:26656,00293ea6d3401f0335c719263b9bff37f8c5a868@65.21.134.202:26566,84bf588ebba53541183998b11b13183971f62ac7@173.249.30.102:26656,a71248b62555f3271df17fb476475cfc7db89275@84.46.240.197:26656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,72a84166fbd6b92d8a772843026cf6a2cd97ffbe@65.109.60.19:46656,55ef009005891c9c8e1291de48297df8bd4ec06f@38.242.203.139:26656,c11a3b8dba22d61e576ff8bc3036c35341490771@65.21.143.116:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
