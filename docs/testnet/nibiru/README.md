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

**live-peers** (39)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,bbc65f7d38f5528cebea9a85020fec5702736da4@90.150.243.196:26656,6df779cceccc7468ceb001ddbd2167471838ca61@149.102.158.241:26656,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,86a825ca58b85e761424a942bb2407be0e7afa16@185.135.137.249:26656,d3091d32c457602c4d3ab348237e56747db81292@77.232.154.215:26656,902bf4fccca9cf97621800e39774c7b7d422ebd0@109.205.180.239:39656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,92e6a5c389e6b27ae52ab3d9c737e7f92ef01e07@89.163.219.90:26656,b1b38341e4d443e2b8d97368c734c1578e4f01cb@46.151.27.109:39656,0caedae543d21fe055dbabc195225b38a48951cd@173.249.0.229:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,63903e6cc8e3c8dd2144caaa7d0249edf526148d@38.242.142.76:39656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,d9d8eb833552b20362ead0d4fdfc13c7ce083d66@194.163.181.120:39656,17d7a3d370413dc134b5f24fff475d78213570ad@207.180.236.124:26656,83856f243eceea02f216e49715a84cf96be6a112@65.109.65.210:33656,c51594d9842de3569c2d440fcefc7a66b2541191@199.175.98.111:36656,f5dcecad06399db3658bfadc2e3d2e8533305d13@135.125.214.61:26656,c04118cc82aca883c2b388bf42e8012276060bb6@155.133.22.113:26656,3a88426d413c9f7794485bdeab5e1cfda1c7430f@77.232.43.194:26656,ab02b0ed1e366ab3746007307d358101965432cb@94.130.55.152:39656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,dba32478d40b2149fc2ae6f74b91ca11b8452da0@38.242.205.130:34656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:39656,0c3c0b937a1f8054794cacd744bf1a13b341508b@113.53.82.252:36656,c859c2b1edfaf67ea274726bc0978ef55ebd051a@94.131.111.156:26656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,8ed5f76e3931d7931dd2d5761ebfea3e7ff895b8@34.130.52.197:26656,874b225ac52fd196ad1d0ecd78e7b505ebc26716@91.229.245.76:26656,73c2805511a8fb700eae740299005c2ff33ec855@45.89.127.44:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,82b5aadfb42e471af43c916d27dbaa2aa28c0bf8@109.123.247.230:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
