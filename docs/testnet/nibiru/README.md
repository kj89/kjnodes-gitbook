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

**live-peers** (41)
```bash
peers="0caedae543d21fe055dbabc195225b38a48951cd@173.249.0.229:26656,bfd1670d642542ff1213b33dd6fb5db1769a17e8@185.234.69.143:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,fe5a3ffcbf6d5958a107ba1e5e8497096b98b863@75.119.153.120:39656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,09c05898d64d2ec387e27ae3e1029a2f53a2a1dc@155.133.22.109:26656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,80b31994a527198278d565d036cda60ce313e0f3@194.180.176.54:26656,b1b38341e4d443e2b8d97368c734c1578e4f01cb@46.151.27.109:39656,8cdbbb2c825856d8738b570859612580da1180c7@212.118.52.21:26656,f978d2dde4b300037c7d2bccb47af9998045bc68@146.0.41.65:39656,73c2805511a8fb700eae740299005c2ff33ec855@45.89.127.44:26656,aa3261d279f300aad20cb30262c910884c3a5b05@178.20.41.240:26656,199a18ce36a79db678abdbb8b767a2792e239101@165.22.212.57:26656,50f70faf399aac827000458d49cdf4ea18f4fb82@95.217.163.250:26656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,8213f67d6cdeaf11742f5d454d4d687023ef2941@5.9.61.237:21656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,e156fef334c3b10ad99399230130e1f5fbcb0cad@95.111.253.90:26656,bcceb73119b08bdaf83121f11a00121cbcbbfe59@185.135.137.244:26656,caaee9953faa9962abb256d5db10a0bd8d4edffb@51.159.187.67:26656,62f26443c930a02f3e166b9db4ecd37b65b042f2@49.12.8.255:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,c7f3b61275dc16993c39a1ebc9f6cb5895d11d56@148.251.43.226:15656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,656465577c4a24380265725e17bffcd13816d6bc@84.46.246.196:26656,162ab520aaacad1d62e3d051246f5fe1ba9dc9c6@65.109.17.23:56112,f5dcecad06399db3658bfadc2e3d2e8533305d13@135.125.214.61:26656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,7e465cf7525009fa55c8387eb74a330d3b96e26f@86.48.5.78:26656,f5b13fb234d28023619755568745ed5c80f63656@86.32.74.154:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
