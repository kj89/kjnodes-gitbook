# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656,d2291c87bdef89c31f8e4008ddc0dee2d2a8ef50@143.244.182.43:26656,ed177ff3cf334df1a6c190438b0c7b5dd64b423a@45.151.122.140:656,1c14a50a931cdf437c1a28bc00565d69950b6c6b@135.181.205.220:36656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,971c22cfb2a8fee7e6b5b7fb125cc9551f3b5e60@65.109.106.91:16656,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,61d2b313e2adc9d7990944f8ab5a6f9ecf08084f@65.21.122.171:16656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,5fa476e097bc0af605581b5fb905b10707c5762d@84.46.247.123:26656,a8591524ebded3132f423771c0d91b77bdffad44@82.208.22.16:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,5c58d5c43b0a93a28da0cd528af7921567a43921@146.190.34.12:41656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,fea7c372588898f7ea3a04373c52a30712b3c279@185.239.209.56:656,d15e22d7be8ba1b97ff429cf87fea2af41450b37@149.102.134.212:41656,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,61af145c3cf74b80f2a7187a55499a3c97e35a8e@38.242.130.204:41656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,05182a9b6121c9fcbb493f9bb3843e20e076e479@38.242.231.113:656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,936d87de95fac39f99fbf7b7ef7b9311a57bffd5@138.68.84.191:26656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,98c3458ef7182730c6402f7f582eef2f77578b8c@185.250.36.151:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
