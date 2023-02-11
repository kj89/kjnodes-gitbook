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
peers="99b57896e917866956f9f078f67f95d6fd6a05e8@161.97.92.139:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,2d953905edc0eeadad8f70a7ead6a6bba327c0ce@173.212.216.232:12656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,d5db3e07270dcfd98fe5f4e9def17c4e9cc2f1d8@89.163.155.216:26656,911a6a9a932f21326e4947d492ff03c405e9039e@65.109.86.236:27656,3a88426d413c9f7794485bdeab5e1cfda1c7430f@77.232.43.194:26656,bec6fe42dd406ac789acb8b52fd6510e56232649@194.163.190.132:12656,10c9aecb4f414d45863cbe1a5f91d04b33fcb638@80.85.242.54:16656,aa3261d279f300aad20cb30262c910884c3a5b05@178.20.41.240:26656,7bbe4afc59fbfff5e6c3189c8ef73a1c6ac3f067@80.82.215.23:26656,f12288a1ed3a9da2c609763be79a0e5bd00e1fb7@167.86.80.145:39656,8e395e5a6082503480bde92720674546f4f1df36@135.181.208.169:26656,9a7689b2ab4d210c3cbc4af27589073823347e50@176.126.87.201:26656,d9020d43390a7d30881a68f65f3247519792a3f0@161.97.85.202:26656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,e84bc060d4d4fe82ea2d7a181f28ddac62b1bb8a@65.109.131.71:26656,dd1b14fefbd55a74baeb8920b34bb7fc15da6b96@62.171.186.61:26656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,db62e60b2a5b4e4139e5a1825acf56876e3b18d5@45.10.154.191:26656,92e6a5c389e6b27ae52ab3d9c737e7f92ef01e07@89.163.219.90:26656,d5006996e18d06892dc244f679171ff52a491b9d@161.97.171.62:26656,657215358614d43e124d0a610c0ffba80e3e10b4@217.76.56.248:26656,e4ea6ffd9ec8ca5db91506e0429613628f0f61ee@155.133.22.115:26656,55ef009005891c9c8e1291de48297df8bd4ec06f@38.242.203.139:26656,c04118cc82aca883c2b388bf42e8012276060bb6@155.133.22.113:26656,e4ea7a21019fe6328e2687137782dff0817263e1@95.31.224.15:26656,c11a3b8dba22d61e576ff8bc3036c35341490771@65.21.143.116:30656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,71a0967b9ce6d0791d603539993a807b8515848d@65.108.56.169:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
