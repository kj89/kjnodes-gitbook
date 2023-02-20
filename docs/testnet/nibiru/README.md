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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,05ea2d5115630db1ec3ba86862d66828eccc2457@91.196.164.143:26656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,b1b38341e4d443e2b8d97368c734c1578e4f01cb@46.151.27.109:39656,049dea10cadfb78ec5e7605809fe5c868e372ab5@149.28.126.247:26656,62f26443c930a02f3e166b9db4ecd37b65b042f2@49.12.8.255:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,32c587c3d9329e6c13c5cd7797eb46b30b628bca@91.107.132.237:26656,a4a0b5b90dbcc92006e7d05d7f6521f120520116@34.75.178.18:26656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,c7f3b61275dc16993c39a1ebc9f6cb5895d11d56@148.251.43.226:15656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,c859c2b1edfaf67ea274726bc0978ef55ebd051a@94.131.111.156:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,022af16bed61bd5749b989695ccfc3870a2238aa@5.199.139.155:39656,df400991447800ca2de270b1ca402d027dab0378@89.163.220.101:26656,139935dfa0a122cfc4a279eef4c5770e278a6196@84.46.246.203:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,283477551bc231c6c473f581e4b34deb82741db8@185.135.137.215:26656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,0c3c0b937a1f8054794cacd744bf1a13b341508b@113.53.82.252:36656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,af77ff768a2e6d7850857a395de566d35ab1c28f@89.163.155.251:39656,2a11b3e06f832e430efb41e3c3bb07a42875d20c@154.53.34.112:26657,50e5bed9efde45f2601e7a63d12d3c8d81e6e7d6@167.86.124.2:26656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,a422bbf59756a9584ddc6f97a8b96bb15b596db7@34.73.61.37:26656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,e545da0d2566c693720992459b002ef75669756c@167.235.204.231:26656,e579409f763fb945569c8d04f0f3257607ab88af@38.242.242.23:26656,e84bc060d4d4fe82ea2d7a181f28ddac62b1bb8a@65.109.131.71:26656,5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
